# My Algorand dApp

## Overview

This repository contains the source code for a Web3 decentralized application (dApp) built on the Algorand Blockchain. The dApp aims to generate and distribute Non-Fungible Tokens (NFTs) as certificates for trainees who successfully complete weekly challenges at 10 Academy. Additionally, it enables trainees with NFTs to interact with a smart contract to perform predefined actions.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Backend](#backend)
  - [Frontend](#frontend)
- [Folder Structure](#folder-structure)
- [Testing](#testing)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## Features

- Algorand Smart Contracts for handling weekly challenges and predefined actions.
- Generation and distribution of NFT certificates to trainees.
- Trainees can opt-in, request, and check the status of NFT transfers.

## Prerequisites

- [react.js] for frontend development.
- [fastAPI] for backend development.
- [Algorand Sandbox] for local testing.
- [Docker] for GitHub Actions.

## Getting Started

### Backend

1. Navigate to the `backend` directory.
2. Install Python dependencies: `pip install -r requirements.txt`.
3. Run the backend: `python app/main.py`.

### Frontend

1. Navigate to the `frontend` directory.
2. Install Node.js dependencies: `npm install`.
3. Run the frontend: `npm start`.

## Folder Structure

- `backend`: Contains the backend FastAPI application.
- `frontend`: Houses the React frontend application.
- `scripts`: Holds deployment and other utility scripts.
- `tests`: Contains frontend, backend, and script tests.
- `.github`: GitHub Actions workflows and configuration.

## License

This project is licensed under the [MIT License](LICENSE).
