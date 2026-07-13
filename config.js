/**
 * AdVerse CRM — runtime config
 *
 * FILL THESE when you connect a real bot + hosting.
 * Safe to commit placeholders; never put secrets in frontend except
 * public bot username / public API base URL.
 */

const APP_CONFIG = {
  /** Public app name */
  appName: "AdVerse",

  /**
   * Bot username WITHOUT @
   * Example: "AdVerseCRM_bot"
   */
  botUsername: "",

  /**
   * HTTPS URL of this Mini App (must match BotFather Web App URL)
   * Example: "https://adverse.example.com"
   */
  miniAppUrl: "",

  /**
   * Optional backend for initData validation & API
   * Example: "https://api.adverse.example.com"
   */
  apiBaseUrl: "https://1c7c87a2f27d4c3b-176-100-6-100.serveousercontent.com",

  /**
   * Endpoint that validates Telegram initData (POST { initData })
   * Leave empty to skip server auth in demo mode
   */
  authEndpoint: "", // e.g. "/api/auth/telegram"

  /**
   * Support chat (opens via Telegram)
   */
  supportUsername: "adverse_support",

  /**
   * Demo: allow role picker even inside Telegram
   * Set false in production when roles come from backend
   */
  allowRolePickerInTelegram: true,

  /**
   * Auto-login when opened from Telegram with valid user
   */
  autoLoginInTelegram: true,

  /**
   * Default role if not set via start_param / backend
   */
  defaultRole: "buyer",
};
