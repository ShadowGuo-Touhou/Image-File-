function handleImage(e) {
    let image = e.files[0];
    if (image.type === "image/png"){
        console.log("yes")
    }

    const imgContainer = document.getElementById("imgContainer"); 
    imgContainer.src = URL.createObjectURL(e.files[0]); 
}