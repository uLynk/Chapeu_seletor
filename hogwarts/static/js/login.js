document.addEventListener("DOMContentLoaded", () => {
    const buttons = document.querySelectorAll(".btn");
    const inputs = document.querySelectorAll("input");

    // Efeito mágico ao clicar nos botões
    buttons.forEach(button => {
        button.addEventListener("click", (event) => {
            let x = event.clientX - button.offsetLeft;
            let y = event.clientY - button.offsetTop;

            let spark = document.createElement("span");
            spark.classList.add("spark");
            spark.style.left = `${x}px`;
            spark.style.top = `${y}px`;
            
            button.appendChild(spark);

            setTimeout(() => {
                spark.remove();
            }, 600);
        });
    });

    // Animação ao focar nos inputs
    inputs.forEach(input => {
        input.addEventListener("focus", () => {
            input.classList.add("focused");
        });

        input.addEventListener("blur", () => {
            input.classList.remove("focused");
        });
    });

    // Validação instantânea
    document.querySelector("form").addEventListener("submit", (event) => {
        let isValid = true;
        inputs.forEach(input => {
            if (input.value.trim() === "") {
                isValid = false;
                input.classList.add("error");
            } else {
                input.classList.remove("error");
            }
        });

        if (!isValid) {
            event.preventDefault();
            alert("Preencha todos os campos!");
        }
    });
});
