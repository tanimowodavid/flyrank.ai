from supabase import create_client, Client
from app.core.config import settings

# Single, shared Supabase client instance used across the entire app
supabase: Client = create_client(settings.SUPABASE_URL, settings.SUPABASE_KEY)
