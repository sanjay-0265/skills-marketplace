function addGig() {
    const title = document.getElementById("title").value;
    const description = document.getElementById("description").value;
    const price = document.getElementById("price").value;

    fetch("/add_gig", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ title, description, price })
    }).then(() => {
        alert("Gig added successfully!");
        location.reload();
    });
}
