import java.io.*;
import java.net.*;

public class Client1 {
    public static void main(String[] args) {
        String serverAddress = "192.168.103.136";
        int port = 9000;

        try (Socket socket = new Socket(serverAddress, port);
             BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
             OutputStream out = socket.getOutputStream();
             InputStream in = socket.getInputStream()) {

            System.out.println("Client 1 connected to the server.");

            // Read the server's request type
            byte[] requestTypeBuffer = new byte[1024];
            int bytesRead = in.read(requestTypeBuffer);
            String requestType = new String(requestTypeBuffer, 0, bytesRead).trim();
            System.out.println("Server requested a " + requestType + " number.");

            // Prompt the user for two numbers based on the request type
            System.out.print("Insert the first number: ");
            String input1 = reader.readLine();
            out.write(input1.getBytes("UTF-8"));

            System.out.print("Insert the second number: ");
            String input2 = reader.readLine();
            out.write(input2.getBytes("UTF-8"));
            out.flush();

            // Wait and read the response from the server
            byte[] serverResponseBuffer = new byte[1024];
            int responseBytes = in.read(serverResponseBuffer);
            String serverResponse = new String(serverResponseBuffer, 0, responseBytes).trim();
            System.out.println("Received from server: " + serverResponse);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
