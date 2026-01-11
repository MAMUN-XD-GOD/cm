const input = document.getElementById("screenshot");

input.addEventListener("change", () => {
  document.getElementById("direction").innerText = "ANALYZING…";
  document.getElementById("expiry").innerText = "—";
  document.getElementById("confidence").innerText = "—";
  document.getElementById("note").innerText = "Chart uploaded. AI reading price structure…";

  // Backend connect point (Phase 12 API)
  setTimeout(() => {
    document.getElementById("direction").innerText = "CALL";
    document.getElementById("expiry").innerText = "1 MIN";
    document.getElementById("confidence").innerText = "78%";
    document.getElementById("note").innerText = "Clean BOS + momentum confirmation";
  }, 1800);
});
