document.addEventListener('DOMContentLoaded', function() {
  const counter = document.getElementById("visitors"); // Use getElementById to directly access the span
  async function updateCounter() {
    try {
      let response = await fetch("https://uzbdwi72ac.execute-api.eu-central-1.amazonaws.com/prod/cloudresume-test-api");
      let data = await response.json();
      counter.innerHTML = data.views; // Assuming 'data.views' is the correct path to the views count
    } catch (error) {
      console.error('Failed to fetch and update counter:', error);
      counter.innerHTML = 'Failed to load views'; // Handle potential null reference here
    }
  }

  updateCounter();
});
