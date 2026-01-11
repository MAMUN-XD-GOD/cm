const input = document.getElementById("screenshot");
const pairInput = document.getElementById("pair");
const timeframeInput = document.getElementById("timeframe");
const winBtn = document.querySelector(".win");
const lossBtn = document.querySelector(".loss");

let lastSignal = null;

async function sendFeedback(result){
  await fetch("http://localhost:5000/feedback", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({
      result,
      signal: lastSignal,
      pair: pairInput.value,
      timeframe: timeframeInput.value
    })
  });
}

input.addEventListener("change", async () => {
  const file = input.files[0];

  document.getElementById("direction").innerText = "ANALYZING…";
  document.getElementById("note").innerText = "AI reading chart…";

  const formData = new FormData();
  formData.append("image", file);
  formData.append("pair", pairInput.value);
  formData.append("timeframe", timeframeInput.value);

  const res = await fetch("http://localhost:5000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();

  document.getElementById("direction").innerText = data.direction;
  document.getElementById("expiry").innerText = data.expiry || "—";
  document.getElementById("confidence").innerText = data.confidence + "%";
  document.getElementById("note").innerText = data.note;

  lastSignal = data.direction;
});

winBtn.onclick = () => sendFeedback("WIN");
lossBtn.onclick = () => sendFeedback("LOSS");
