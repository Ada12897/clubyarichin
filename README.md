<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>AI Интерьер</title>
  <style>
    body {
      font-family: sans-serif;
      max-width: 600px;
      margin: 30px auto;
      text-align: center;
    }
    #preview {
      max-width: 100%;
      margin-top: 10px;
      border-radius: 10px;
    }
    #result {
      max-width: 100%;
      margin-top: 20px;
      border: 2px solid #ddd;
      border-radius: 10px;
    }
    button {
      margin-top: 15px;
      padding: 10px 20px;
      font-size: 16px;
      cursor: pointer;
    }
  </style>
</head>
<body>
  <h1>AI Дизайн комнаты</h1>
  <p>Загрузи фото своей комнаты — нейросеть сделает редизайн</p>

  <input type="file" id="fileInput" accept="image/*"><br>
  <img id="preview" src="" alt="Предпросмотр" hidden>
  <button id="generateBtn" disabled>Создать новый дизайн</button>

  <h3>Результат:</h3>
  <img id="result" src="" alt="AI результат" hidden>

  <script>
    const fileInput = document.getElementById('fileInput');
    const preview = document.getElementById('preview');
    const result = document.getElementById('result');
    const button = document.getElementById('generateBtn');

    fileInput.addEventListener('change', () => {
      const file = fileInput.files[0];
      if (!file) return;
      preview.src = URL.createObjectURL(file);
      preview.hidden = false;
      button.disabled = false;
    });

    button.addEventListener('click', async () => {
      const file = fileInput.files[0];
      if (!file) return alert('Сначала выбери фото!');
      button.textContent = 'Генерация...';
      button.disabled = true;

      const formData = new FormData();
      formData.append('image', file);
      formData.append('room', 'bedroom');
      formData.append('theme', 'modern');

      try {
        const res = await fetch('https://api.roomgpt.io/api/v1/rooms', {
          method: 'POST',
          body: formData
        });
        const data = await res.json();
        result.src = data.imageUrl;
        result.hidden = false;
      } catch (err) {
        alert('Ошибка при запросе к API: ' + err);
      } finally {
        button.textContent = 'Создать новый дизайн';
        button.disabled = false;
      }
    });
  </script>
</body>
</html>
