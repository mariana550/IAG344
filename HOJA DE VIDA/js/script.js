function downloadPDF(){
    const element = document.querySelector('#pdf-content');
    //console.log(element);
    const opt = {
        margin: [5, 10, 5, 10], //[arriba, izquierda, abajo, derecha] en mm
        filename: 'Hoja_de_vida_Mariana_Villegas.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas:{
            scale: 2,
            useCORS: true,
            scrollY:0,
            allowTaint: true
        },
        jsPDF:{
            unit:'mm',
            format:'a4',
            orientation:'portrait' //Orientación vertical
        }
    };
    html2pdf().set(opt).from(element).save();    
}