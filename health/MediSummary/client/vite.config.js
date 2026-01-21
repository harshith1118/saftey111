import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// https://vite.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/generate': 'https://medisummary-702123324614.us-central1.run.app',
    },
  },
})
