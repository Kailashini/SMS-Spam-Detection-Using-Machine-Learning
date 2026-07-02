document.addEventListener("DOMContentLoaded", () => {

    const form = document.querySelector("form");

    form.addEventListener("submit", function () {

        const message = document.querySelector("textarea").value.trim();

        if (message === "") {

            alert("Please enter an SMS message.");

            return false;

        }

    });

});