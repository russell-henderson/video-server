/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        base: {
          DEFAULT: '#0b0f14',
          50: '#0b0f14',
          100: '#111726',
          200: '#1a2335',
          300: '#223049'
        },
        glow: {
          blue: '#5bc9ff',
          gold: '#ffc56b',
          rose: '#ff97b3'
        },
        glass: 'rgba(255,255,255,0.06)'
      },
      backdropBlur: { xs: '2px' },
      boxShadow: { glow: '0 0 40px rgba(91,201,255,0.15)' }
    }
  },
  plugins: []
}
