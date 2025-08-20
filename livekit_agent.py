from dotenv import load_dotenv
from livekit.agents import (
    AgentSession,
    Agent,
    JobContext,
    WorkerOptions,
    cli,
    RoomInputOptions
)
from livekit.plugins import elevenlabs, noise_cancellation, silero, openai
from livekit.plugins.turn_detector.multilingual import MultilingualModel
from livekit.plugins import langchain

from langgraph_agent import create_workflow

load_dotenv()

class Assistant(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful assistant.")

async def entrypoint(ctx: JobContext):
    
    session = AgentSession(
        llm=langchain.LLMAdapter(
            graph=create_workflow() 
        ),
        stt=openai.STT(model="whisper-1",detect_language=True),
        tts=elevenlabs.TTS(model="eleven_flash_v2_5",voice_id="yj30vwTGJxSHezdAGsv9"),
        turn_detection=MultilingualModel(), 
        vad=silero.VAD.load(),
        preemptive_generation=True,
    )

    await session.start(
        agent=Assistant(),
        room=ctx.room,
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()


if __name__ == "__main__":
    cli.run_app(WorkerOptions(entrypoint_fnc=entrypoint))