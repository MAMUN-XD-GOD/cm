function send() {
  const f = document.getElementById("img").files[0];
  const fd = new FormData();
  fd.append("image", f);

  fetch("/analyze", {
    method: "POST",
    body: fd
  })
  .then(r => r.json())
  .then(d => {
    document.getElementById("out").textContent =
      JSON.stringify(d, null, 2);
  });
}
