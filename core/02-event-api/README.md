# Weather App (Vite + React)

This project displays the current weather in London using the OpenWeatherMap API.

## File Details

- `src/app.jsx` – Main React component, displays weather info.
- `src/weather.jsx` – API helper for fetching weather data.
- `src/main.jsx` – Entry point
- `src/index.css` – styles
- `index.html` – Main HTML file.
- `.env` – API key for OpenWeatherMap

## Setup

1. Install dependencies:
   ```sh
   npm install
   ```

2. Add your OpenWeatherMap API key to `.env`:
   ```
   VITE_WEATHER_API_KEY=your_api_key_here
   ```

3. Start the development server:
   ```sh
   npm run dev
   ```

4. Visit [http://localhost:5173](http://localhost:5173) in your browser.

## Notes

- Weather data is fetched for London, UK.
- Requires a valid OpenWeatherMap API key in `.env`.
