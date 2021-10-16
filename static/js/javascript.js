(function(win,doc){
    'use strict';
//Verifica se o usuário realmente quer deletar o dado
    if(doc.querySelector('.btnDel')){
        let btnDel = doc.querySelectorAll('.btnDel');
        for(let pk=0; pk < btnDel.length; pk++){
            btnDel[pk].addEventListener('click', function(event){
                if(confirm('Deseja mesmo apagar este dado?')){
                    return true;
                }else{
                    event.preventDefault();
                }
            });
        }
    }
})(window,document);