{"user interface for weather application"}
{"imports fetchWeather function from weather.jsx"}

{"keeps updating info about weather in london"}
import { useEffect, useState } from 'react';
{"when program runs, fetches weather data"}
import { fetchWeather } from './weather';

function App() {
  const [weather, setWeather] = useState(null);

  useEffect(() => {
    fetchWeather().then(setWeather).catch(console.error);
  }, []);

  if (!weather) return <p>Loading...</p>;

  return (
    <div>
      <h1>London Weather</h1>
      <p>Temperature: {weather.main.temp}°C</p>
      <p>Conditions: {weather.weather[0].description}</p>
    </div>
  );
}

export default App;
