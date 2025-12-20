from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import List, Optional

class Settings(BaseSettings):
    APP_NAME: str = "SAYeTECH Investor Dataroom"
    MONGODB_URL: str
    DATABASE_NAME: str
    
    # Brevo (Sendinblue) Configuration
    BREVO_API_KEY: str
    BREVO_SENDER_EMAIL: str
    BREVO_SENDER_NAME: str
    
    # SMTP Configuration for sayetech.io
    SMTP_HOST: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str
    FROM_EMAIL: str
    SMTP_USE_TLS: bool
    SMTP_USE_SSL: bool
    
    # Admin Configuration
    ADMIN_EMAIL: str
    
    # Security
    SECRET_KEY: str
    OTP_EXPIRY_MINUTES: int
    OTP_MAX_ATTEMPTS: int
    OTP_LENGTH: int
    
    # File Upload
    UPLOAD_DIR: str
    MAX_FILE_SIZE_MB: int
    ALLOWED_EXTENSIONS: List[str]
    ALLOWED_FILE_TYPES: List[str]
    NDA_VERSION: str
    
    # Redis Cache
    REDIS_URL: str
    CACHE_TTL: int
    
    # Slack Integration
    SLACK_WEBHOOK_URL: str
    
    # Meeting Scheduler
    CALENDLY_API_KEY: str
    
    # Cloudinary Configuration
    CLOUDINARY_CLOUD_NAME: str
    CLOUDINARY_API_KEY: str
    CLOUDINARY_API_SECRET: str
    
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()
