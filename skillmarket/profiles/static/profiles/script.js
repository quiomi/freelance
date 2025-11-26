
(function(){
      const hire = document.getElementById('hireBtn');
      const msg = document.getElementById('messageBtn');
      hire.addEventListener('click', ()=>{
        hire.animate([{transform:'translateY(0)'},{transform:'translateY(-4px)'},{transform:'translateY(0)'}],{duration:350,easing:'ease-out'});
        hire.textContent = 'Request sent';
        setTimeout(()=>hire.textContent = 'Hire',2000);
      });
      msg.addEventListener('click', ()=>{
        msg.animate([{opacity:1},{opacity:.6},{opacity:1}],{duration:350});
      });

    })();