class="form-row field-email_address field-email_label"


const elementsToRemove = document.querySelectorAll('.field-email_address .field-email_label');

// Loop through the selected elements and remove the HTML block
elementsToRemove.forEach(element => {
  element.innerHTML = '';
});