
# PSA Process (Client-Server)

This repository implements a privacy-preserving Set Intersection (PSA) protocol using a client-server architecture. The process involves multiple Python scripts that perform the necessary operations to compute the intersection securely across clients and the server.

## Participants

There are two main participants in the PSA process: **Client** and **Server**.

### 1. **Client**:
The Client's main role is to perform the initial setup, send data to the server for intersection calculation, and receive results from the server. 

#### Client Tasks:
- **Data Generation**: 
  - The `generate_data.py` script is used by each client to generate a random dataset for processing.
- **Data Initialization and Upload**: 
  - The `mapping.py` script initializes the data and uploads it to the server.
- **Client Aggregation**: 
  - After the server performs calculations and requests client-side aggregation, the client uses the `client_agg.py` script to compute and return the aggregation result to the server.
- **GS Protocol**:
  - In the T-PSA process, the client executes `client_gs.py` to initialize data and send the calculation task to the server.

### 2. **Server**:
The server is responsible for receiving the client data, performing computations, and requesting intermediate results from the clients.

#### Server Tasks:
- **Server Setup**:
  - The server is initialized and ready to accept data by running `fla_server.py`.
- **Intersection Calculation**:
  - The server uses `server_lew.py` to perform the intersection calculations, interacting with the client to get aggregation values.
- **Final Aggregation**:
  - After receiving data from the client, the server aggregates the results using `server_agg.py`.
- **GS Protocol**:
  - In the T-PSA process, the server receives data and computations from the client using `fla_gs.py` and then uses `server_gs.py` to perform calculations for the final result.


## Running the T-PSA Process

### Client-Side:
1. **Step 1**: Run `generate_data.py` to generate the random dataset.
2. **Step 2**: Use `mapping.py` to initialize and upload the dataset to the server.
3. **Step 3**: Wait for the server to initiate intersection calculation. Once the request is received, run `client_agg.py` to perform the aggregation and send it back to the server.
4. **Step 4 (T-PSA)**: Run `client_gs.py` to initialize data and send the task to the server for T-PSA processing.

### Server-Side:
1. **Step 1**: Start the server by running `fla_server.py`.
2. **Step 2**: The server will wait for the client to upload data. Upon receiving data, it will run `server_lew.py` to compute the intersection with the clients' data.
3. **Step 3**: Request aggregation from the clients and perform the aggregation calculation using `server_agg.py`.
4. **Step 4 (T-PSA)**: After receiving client data for T-PSA, run `fla_gs.py` to process the data and `server_gs.py` to finalize the result.

## Setup and Requirements

- Python 3.x
- Dependencies can be installed using `pip` (install the required libraries as necessary).

## Notes

- Ensure that the client and server are on the same local area network (LAN) or have proper communication channels over a wide area network (WAN).
- Data privacy is maintained throughout the PSA process.
