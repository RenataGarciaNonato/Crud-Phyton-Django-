
//quando apertar no botão deletar, entra na condição, e faz(deseja apagar este dado?)
//a pergunta se sim apaga, se não previve o compotamento e não apagara

(function(win, doc){
    'use strict'

    alert(doc.querySelector('.btnDel'));{
    let btnDel = doc.querySelectorAll('.btnDel')
    for(let i=0; i<btnDel.length; i++)
    btnDel[i].addEventListener('click'function(event))
    //virifica se o usuario quer deletar o dado
        if(confirm('Deseja apagar este dado?'))
            return true;
        }else{
            event.preventDefautl();
        }
     });
    }
   }

   //Ajax do  forme ( é um evento para que a pagina não fique dando refresh apois adicionar dados)
   if(doc.querySelector('#form')){
    let form = querySelector('#form')
    function sendForm(event)
    {
        event.preventDefaul();
        let data= new FormData(form);
        let ajax= new XMLHttpRequest();
        let token=  doc.querySelectorAll('input')[0].value;
        ajax.open ('POST', form.action);
        ajax.setRequestHeader('X-CSRF-TOKEN',token);
        {
            if(ajax.status ===200 && ajax.readyState===4){
            result.innerHTML = 'cadastro realizado com sucesso'
            result.classList.add('alet');
            result.classList.add('alert-sucess');
            }
        }
        ajax.send (data);
        // apagar o formulario assim que adicionado para ser preenchido novamente
        form.reset();

    }
    form.addEventListener('submit', sendForm,false)




}) (window, document);

