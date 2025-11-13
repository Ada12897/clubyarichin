<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <title>AI Дизайн комнаты</title>
  <style>
    body {
      font-family: sans-serif;
      text-align: center;
      max-width: 600px;
      margin: 30px auto;
    }
    img { max-width: 100%; border-radius: 10px; margin-top: 10px; }
    button { padding: 10px 20px; margin-top: 15px; font-size: 16px; cursor: pointer; }
  </style>
</head>
<body>
  <h1>AI дизайн комнаты</h1>
  <p>Загрузи фото — получи редизайн интерьера</p>

  <input type="file" id="fileInput" accept="image/*">
  <img id="preview" hidden>
  <button id="generateBtn" disabled>Сделать редизайн</button>

  <h3>Результат:</h3>
  <img id="result" hidden>

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
      if (!file) return alert('Выбери фото!');
      button.textContent = 'Генерация...';
      button.disabled = true;

      // используем готовый публичный API (Replicate)
      const formData = new FormData();
      formData.append("image", file);

      try {
        const res = await fetch("https://replicate-api-proxy.glitch.me/generate", {
          method: "POST",
          body: formData
        });
        const data = await res.json();
        result.src = data.output_url;
        result.hidden = false;
      } catch (err) {
        alert("Ошибка: " + err);
      } finally {
        button.textContent = "Сделать редизайн";
        button.disabled = false;
      }
    });
  </script>
</body>
</html>
