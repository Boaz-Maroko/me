document.addEventListener('DOMContentLoaded', function () {
    const toggleButton = document.getElementsByClassName('toggle-button')[0];
    const navbarLinks = document.getElementsByClassName('navbar-links')[0];


    toggleButton.addEventListener('click', () => {
        navbarLinks.classList.toggle('active');
    });
});


document.addEventListener( 'DOMContentLoaded', function (){
    const wrapper = document.getElementsByClassName('wrapper')[0];
    const textarea = document.getElementsByClassName('message')[0]
    const tabs = document.getElementsByClassName('navbar-links');
    const submitBtn = document.getElementById('send-message');
    const emailBox = document.getElementsByClassName('email')[0];

    function checkActiveStatus() {
        const navbarLinks = document.getElementsByClassName('navbar-links')[0];

        if (navbarLinks.classList.contains('active')){
            navbarLinks.classList.remove('active');
        }
    }

    function highlightTab() {
        let tabsArray = Array.from(tabs)

        for (let tab of tabsArray) {
            tab.classList.add('active')

        }
    }



    wrapper.addEventListener('wheel', checkActiveStatus);
    wrapper.addEventListener('click', checkActiveStatus);
    textarea.addEventListener('input', function (event){
        if (event.target.value === ""){
            this.style.height = '50px'
        }

        this.style.height = this.scrollHeight + 'px'


    });

    textarea.addEventListener('focus', function (){

        this.style.backgroundColor = '#dddddd'

    });

    submitBtn.addEventListener('click', function (){
        alert("sent")
    })

})
