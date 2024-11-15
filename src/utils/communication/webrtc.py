import asyncio
import json
from typing import Dict, Any, List, TYPE_CHECKING
from aiortc import RTCPeerConnection, RTCSessionDescription, RTCDataChannel

class WebRTCCommUtils(CommunicationInterface):
    def __init__(self, config: Dict[str, Dict[str, Any]]):
        #signaling for peer id and establishing connection?
        pass

    async def send_message(self, data_channel: RTCDataChannel, message_type: str, message: Any) -> None:
        """Send a message using the data channel."""
        if data_channel.readyState == "open":
            data_channel.send(json.dumps({"type": message_type, "data": message}))
            print(f"Sent: {message}")
        else:
            print("DataChannel is not open yet.") 

    """
    Idea: 
    - request_data:
        peer 1 wants to request data from peer 2, peer 1 will open
        channel and send a "type": "request: message to peer 2
    - send_data:
        when peer 2 sees a message of "type": "request", peer 2 will
        open channel and send data back to peer 1
    """

    async def send(self, data: Any):
        pc = RTCPeerConnection()
        data_channel = pc.createDataChannel("chat") #type: ignore

        # Handle incoming messages
        @data_channel.on("message") #type: ignore
        def on_message(message: Any):
            print(f"Received: {message}")
            try:
                data = json.loads(message)
                if data.get("type") == "request":
                    print(f"Request received: {data.get('data')}")
                    response = "Here is the information you requested"
                    asyncio.get_event_loop().call_later(2, lambda: asyncio.ensure_future(send_message(data_channel, "data", response)))
                    # self.send_message(data_channel, "data", response)
                    print(f"Response sent: {response}")
            except json.JSONDecodeError:
                print("Invalid message format received.")

        # Signal when the data channel is open
        @data_channel.on("open") #type: ignore
        def on_open():
            print("DataChannel is open and ready to receive requests.")

        # Create and send an SDP offer
        offer = await pc.createOffer()
        await pc.setLocalDescription(offer)
        print("SDP offer created.")
        # (Signaling exchange code to send the offer and receive an answer would go here)

    async def receive(self):
        pc = RTCPeerConnection()

        # Handle incoming data channels
        @pc.on("datachannel")
        def on_datachannel(channel: RTCDataChannel):
            print("DataChannel received.")

            # Send a request once the channel is open
            @channel.on("open")
            def on_open():
                print("DataChannel is open.")
                request = {"type": "request", "data": "Please send me some data"}
                channel.send(json.dumps(request))
                print(f"Request sent: {request}")

            # Handle responses
            @channel.on("message")
            def on_message(message: str):
                print(f"Received: {message}")

        # Receive SDP offer and send SDP answer
        # (Signaling exchange code to receive the offer, set the remote description,
        # create the answer, and send it back would go here)