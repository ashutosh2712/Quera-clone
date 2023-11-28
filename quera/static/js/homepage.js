function showPostForm() {
    document.querySelector(".post-form").style.display = "block";
  }
  function closePostForm() {
    document.querySelector(".post-form").style.display = "none";
  }

  function showAnswerForm(questionId) {
    if (Number.isInteger(questionId) && questionId > 0) {
      document.getElementById("overlay").style.display = "block";
      document.getElementById("answerModal").style.display = "block";

      document.querySelector(
        "#answerModal form"
      ).action = `/quera/postans/${encodeURIComponent(questionId)}/`;
    } else {
      console.error("Invalid questionId:", questionId);
    }
  }

  function closeAnswerForm() {
    document.getElementById("overlay").style.display = "none";
    document.getElementById("answerModal").style.display = "none";
  }

  document.querySelectorAll(".upvote-btn").forEach((button) => {
    button.addEventListener("click", () =>
      handleVote("upvote", button.dataset.answerId)
    );
  });

  document.querySelectorAll(".downvote-btn").forEach((button) => {
    button.addEventListener("click", () =>
      handleVote("downvote", button.dataset.answerId)
    );
  });

  function handleVote(action, answerId) {
    fetch(`/quera/${action}/${answerId}/`)
      .then((response) => response.json())
      .then((data) => {
        const answerElement = document.querySelector(
          `[data-answer-id="${answerId}"]`
        );
        const upvoteCountElement = answerElement.querySelector(".upvote-count");
        upvoteCountElement.textContent = data.upvotes;
      })
      .catch((error) => console.error("Error:", error));
  }