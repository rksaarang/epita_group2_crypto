import os
from dataclasses import dataclass
from dotenv import load_dotenv

# Load variables from the local .env file
load_dotenv()


@dataclass(frozen=True)
class Settings:
    app_env: str = os.getenv("APP_ENV", "development")
    api_key: str = os.getenv("CRYPTOCOMPARE_API_KEY", "")
    debug: bool = os.getenv("DEBUG", "False").lower() in ("true", "1", "yes")

    def validate(self):
        """Check that the API key is configured."""
        if not self.api_key or self.api_key.startswith("your_"):
            raise ValueError(
                "CRITICAL SECURITY / CONFIG ERROR: API key is not configured!\n"
                "Ensure your .env file exists and contains a valid API key."
            )


config = Settings()