document.addEventListener('DOMContentLoaded', function() {
  const innerBoxes = document.querySelectorAll('.inner-box');

  innerBoxes.forEach(innerBox => {
    const decrementButton = innerBox.querySelector('#decrement');
    const incrementButton = innerBox.querySelector('#increment');
    const countElement = innerBox.querySelector('#count');

    // Retrieve count from local storage or default to 0
    let count = parseInt(localStorage.getItem('count')) || 0;

    // Update the initial count display
    updateCount();

    decrementButton.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent form submission
      count = Math.max(0, count - 1);
      updateCount();
    });

    incrementButton.addEventListener('click', function(event) {
      event.preventDefault(); // Prevent form submission
      if (count < 5) { // Check if count is less than 5 before incrementing
        count++;
        updateCount();
      }
    });

    function updateCount() {
      // Update the count display
      countElement.textContent = count;
      // Store the count in local storage
      localStorage.setItem('count', count.toString());
    }
  });
});
