const input = document.getElementById("screenshot");

input.addEventListener("change", async () => {
  const file = input.files[0];

  document.getElementById("direction").innerText = "ANALYZING…";
  document.getElementById("note").innerText = "AI reading chart…";

  const formData = new FormData();
  formData.append("image", file);

  const res = await fetch("http://localhost:5000/analyze", {
    method: "POST",
    body: formData
  });

  const data = await res.json();

  document.getElementById("direction").innerText = data.direction || data.signal;
  document.getElementById("expiry").innerText = data.expiry || "—";
  document.getElementById("confidence").innerText = data.confidence
    ? data.confidence + "%"
    : "—";

  document.getElementById("note").innerText = data.note || "Analysis complete";
});
