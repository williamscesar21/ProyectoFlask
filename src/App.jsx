import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Header from './header';

const App = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState(null);
  const apiUrl = 'http://localhost:9090/libreria/verLibros';

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await axios.get(apiUrl);
        setData(response.data);
      } catch (error) {
        setError('Error fetching data from the API');
      }
    };

    fetchData();
  }, [apiUrl]);

  return (
    <>
    <Header/>
      {error && <div>Error: {error}</div>}
      {!error && data.length > 0 && (
        <div style={{ display: 'flex', flexWrap: 'wrap', justifyContent: 'center' }}>
          {data.map((libro) => (
            <div key={libro.Id_del_libro} className="book-card">
              <strong>{libro.Nombre_del_libro}</strong><br />
              Autor: {!libro.Nombre_del_autor?<> Autor desconocido </>: libro.Nombre_del_autor }<br />
              Género: {!libro.Nombre_del_genero?<> Genero no determinado </>: libro.Nombre_del_genero }<br />
              Reseña: {!libro.Texto_de_la_reseña?<> Sin reseñas </>: libro.Texto_de_la_reseña }<br />
              {(!libro.Texto_de_la_reseña || !libro.Usuario_de_la_reseña)?null:<>Usuario de la reseña: {libro.Usuario_de_la_reseña}</>}
            </div>
          ))}
        </div>
      )}
    </>
  );
};

export default App;
