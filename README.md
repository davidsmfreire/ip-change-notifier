# ip-change-notifier

Service that sends a notification to your phone through Signal whenever the public IPV4 of its host changes.

## How to use

1. Create and modify .env based on .env.example

    ```console
    cp .env.example .env
    ```

2. Run service

    ```console
    docker compose up -d
    ```
