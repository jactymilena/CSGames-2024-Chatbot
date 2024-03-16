const chatForm = get('form');
const chatInput = get('input');
const chatBox = get('main');

appendMessage('bot', 'This is a bot that will help you identify your health problems according to your symptoms. Feel free to ask any question.');
appendMessage('bot', 'What are your symptoms.');

// appendMessage('user', 'This is a user bubble');

chatForm.addEventListener('submit', event => {
  event.preventDefault();
  const text = chatInput.value;
  if (!text) return;
  
  appendMessage('user', text);
  test(text);
  
  chatInput.value = '';
});

function test(text) {
  console.log(text);
  fetch("http://127.0.0.1:5000/docus", 
  {
      method: 'POST',
      headers: {
          'Content-type': 'application/json',
          'Accept': 'application/json'
      },
      body:JSON.stringify(text)}).then(res=>{
          if(res.ok){
              return res.json()
          }else{
              alert("something is wrong")
          }
      }).then(jsonResponse=>{
          // Log the response data in the console
          console.log(jsonResponse)
          console.log("Here we log the response")
          appendMessage('bot', jsonResponse["data"])
      } 
      ).catch((err) => console.error(err));
      
}
  
function appendMessage(side, text) {
  const bubble = `
    <div class="msg -${side}">
        <div class="bubble">${text}</div>
    </div>`;
  chatBox.insertAdjacentHTML('beforeend', bubble);
  chatBox.scrollTop += 500;
}

// Utils
function get(selector, root = document) {
  return root.querySelector(selector);
}
