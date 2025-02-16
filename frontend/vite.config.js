import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        // Rewrite the URL: remove the '/api' prefix
        rewrite: (path) => path.replace(/^\/api/, ''),
      },
    },
  },
});
