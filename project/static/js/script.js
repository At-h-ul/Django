// Your external JavaScript file

document.addEventListener("DOMContentLoaded", function() {
  const form = document.getElementById("signup-form");
  const emailInput = document.getElementById("email");
  const passInput = document.getElementById("password");
  const Pass1Input = document.getElementById("password1");

  form.addEventListener("submit", function(e) {
    e.preventDefault();
    checkEmail();
    createPass();
    confirmPass();

    if (!document.querySelector(".email-field").classList.contains("invalid") &&
        !document.querySelector(".create-password").classList.contains("invalid") &&
        !document.querySelector(".confirm-password").classList.contains("invalid")) {
      form.submit();
    }
  });

  emailInput.addEventListener("keyup", checkEmail);
  passInput.addEventListener("keyup", createPass);
  cPassInput.addEventListener("keyup", confirmPass);

  const eyeIcons = document.querySelectorAll(".show-hide");

  eyeIcons.forEach((eyeIcon) => {
    eyeIcon.addEventListener("click", () => {
      const pInput = eyeIcon.parentElement.querySelector("input");
      if (pInput.type === "password") {
        eyeIcon.classList.replace("bx-hide", "bx-show");
        pInput.type = "text";
      } else {
        eyeIcon.classList.replace("bx-show", "bx-hide");
        pInput.type = "password";
      }
    });
  });

  function checkEmail() {
    const emailPattern = /^[^ ]+@[^ ]+\.[a-z]{2,3}$/;
    if (!emailInput.value.match(emailPattern)) {
      document.querySelector(".email-field").classList.add("invalid");
    } else {
      document.querySelector(".email-field").classList.remove("invalid");
    }
  }

  function createPass() {
    const passPattern = /^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$/;
    if (!passInput.value.match(passPattern)) {
      document.querySelector(".create-password").classList.add("invalid");
    } else {
      document.querySelector(".create-password").classList.remove("invalid");
    }
  }

  function confirmPass() {
    if (passInput.value !== Pass1Input.value || Pass1Input.value === "") {
      document.querySelector(".confirm-password").classList.add("invalid");
    } else {
      document.querySelector(".confirm-password").classList.remove("invalid");
    }
  }
});
