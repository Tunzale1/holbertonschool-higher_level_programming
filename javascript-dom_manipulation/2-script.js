let redHeaderElement = document.getElementById('red_header');

redHeaderElement.addEventListener('click', function() {
    document.querySelector('header').classList.add('red');
});
