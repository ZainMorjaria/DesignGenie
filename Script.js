async function generate() {
  const prompt = document.getElementById("promptInput").value;

  const res = await fetch(`http://127.0.0.1:8000/generate?prompt=${encodeURIComponent(prompt)}`);
  const data = await res.json();

  document.getElementById("result").innerText = data.result;
}

async function generateImage() {
  const prompt = document.getElementById("imagePrompt").value;

  const res = await fetch(`http://127.0.0.1:8000/generate-image?prompt=${encodeURIComponent(prompt)}`);
  const data = await res.json();

  const img = document.getElementById("imageResult");
  img.src = data.image_url;
  img.style.display = "block";
}
