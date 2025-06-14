function moWeek() {
    this.model = document.getElementById('LogInSignTabs');
    this.signUp_footer = document.getElementById('SignUpFooter')
    this.LogIn_footer = document.getElementById('LogInFooter')
    this.signin_Ways = [
        { site: "google", link: '#', imageUrl: 'static/images/SignIn_icons/icons8-gmail-48.png' },
        { site: "facebook", link: '#', imageUrl: 'static/images/SignIn_icons/icons8-facebook-48.png' }
    ]
}

moWeek.prototype.render = function () {

    this.signin_Ways.forEach(element => {
        const { site, link, imageUrl } = element;
        const templet = `<a id = "SignIn-alt" href=${link}>
                            <img src="${imageUrl}"><span id="SignInTemplates" >Signup with ${site}</span>
                         </a>`

        let Modelfooter = document.createElement('div');
        Modelfooter.setAttribute('class', 'col')
        Modelfooter.innerHTML = templet;
        this.signUp_footer.appendChild(Modelfooter);
    });

    this.signin_Ways.forEach(element => {
        const { site, link, imageUrl } = element;
        const templet = `<a id = "SignIn-alt" href=${link}>
                            <img src="${imageUrl}"><span id="SignInTemplates" >Signin with ${site}</span>
                         </a>`

        let Modelfooter = document.createElement('div');
        Modelfooter.setAttribute('class', 'col')
        Modelfooter.innerHTML = templet;
        this.LogIn_footer.appendChild(Modelfooter);
    });
}

const moWeekInstance = new moWeek();
moWeekInstance.render();