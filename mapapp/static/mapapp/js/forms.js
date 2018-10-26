document.addEventListener('DOMContentLoaded', function () {
    // Initialize select field
    let $select = document.querySelector('select');
    M.FormSelect.init($select);

    // Initialize select field
    let $modal = document.querySelector('.modal');
    M.Modal.init($modal);

    const flashCloseButton = document.querySelector('.flash-close');
    
    // Click event on flash message
    flashCloseButton &&
        flashCloseButton.addEventListener("click", function () {
            const flashMessage = document.querySelector('.messages');
            flashMessage.parentNode.removeChild(flashMessage);
        });
});