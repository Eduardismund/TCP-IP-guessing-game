## Guess the Number Game (Chaos Edition)

This is a simple multiplayer game where a server generates a random number, and multiple clients connect to guess it. Each client sends a guess, and the server responds with hints like "higher," "lower," or "correct." However, there’s a twist: the server might occasionally lie, making the game more unpredictable as players decide whether to trust the hints or rely on their intuition.

---

## Technology Stack

- **Server**: Implemented in **Python**.
- **Clients**: Implemented in **Java**.

This cross-language setup demonstrates the flexibility of TCP/IP, allowing clients and servers to communicate across different programming languages.

---

## How TCP Supports Concurrent Users

The game uses **TCP (Transmission Control Protocol)** to maintain reliable, ordered communication between the server and clients. TCP’s persistent connections allow multiple clients to connect and play at the same time. When each client connects, the server creates a new process, enabling **concurrent gameplay** without interference between players. TCP ensures each guess and hint is delivered accurately, providing a smooth and interactive gaming experience.

---

## How It Works

1. **Python Server**: The server is written in Python and listens on a specified port for incoming connections from clients. When a client connects, the server forks a new process to handle that client, allowing multiple clients to connect and play concurrently.

2. **Java Clients**: Each client is implemented in Java and connects to the server over TCP. The clients send guesses to the server and receive hints in response. The Java clients handle server responses to keep gameplay smooth and engaging.

This setup allows for real-time multiplayer interaction, with clients and the server communicating seamlessly across different programming environments.
