document.addEventListener('DOMContentLoaded', function () {
    // Initialize select field
    let $select = document.querySelector('select');
    M.FormSelect.init($select);

    // Initialize select field
    let $modal = document.querySelector('.modal');
    M.Modal.init($modal);
});