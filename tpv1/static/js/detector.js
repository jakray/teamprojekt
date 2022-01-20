









function Detector () {
    // for the conditional rendering of the status bar with rueckgabe
    const [value, setValue] = useState(0);
    const [hasValue, setHasValue] = useState(false);

    const clickbaitInput = useRef();

    async function clickbaitHandler(event) {
            event.preventDefault();
            const enteredSentence = clickbaitInput.current.value;
            const reqBody = {text :  enteredSentence}
            clickbaitInput.current.value = "";
            
            const newData = fetch('http://ec2-3-67-188-23.eu-central-1.compute.amazonaws.com:8100/h',{
                method:"POST",
                mode:'cors',
                body: JSON.stringify(reqBody),
                headers:{"Content-Type":"application/json",
                }

            })

            
            .then((response) => response.json())
            .then((data) => console.log(data))
            .then((data => setValue(data)))
            // nur zum testen
            .then(setValue(20))
            .then(setHasValue(true))
            .then(console.log(value))
            .catch(error => {
                console.error('Error:', error);
                throw error;
            })
    }
    

    

    
    function move() {
        var i = 0;
        if (i == 0) {
        i = 1;
        var elem = document.getElementById("myBar");
        var width = 1;
        var id = setInterval(frame, 100);
        function frame() {
          if (width >= value) {
            clearInterval(id);
            i = 0;
          } else {
            width++;
            elem.style.width = width + "%";
            elem.innerHTML = width + "%";
          }
        }
    }
}}