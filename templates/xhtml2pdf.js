
    var element = document.getElementById('to_print');
    var opt = {
        margin: [20, 20, 20, 20],
        filename: 'file.pdf',
        image: { type: 'jpeg', quality: 0.98 },
        html2canvas: { scale: 5 },
        jsPDF: { unit: 'pt', format: 'a4', orientation: 'portrait' },
        // pagebreak: {avoid: 'div' }
    };
    // New Promise-based usage:
    // html2pdf().set(opt).from(element).save();


    // html2pdf().set(opt).from(element).toPdf().output('blob').then((data) => {
    //     console.log(data)
    //     let fileURL = URL.createObjectURL(data);
    //     window.open(fileURL);
    // })
    html2pdf().from(element).set(opt).toPdf().get('pdf').then(function(pdf) {
    var totalPages = pdf.internal.getNumberOfPages();
    for (i = 1; i <= totalPages; i++) {
        pdf.setPage(i);
        pdf.setFontSize(10);
        pdf.setTextColor(100);
        pdf.text('Devis Réf: D-A234-2301-001 - Page ' + i + ' of ' + totalPages, (pdf.internal.pageSize.getWidth() / 1.5), (pdf.internal.pageSize.getHeight() - 10));
    }
}).save();



// var element=document.getElementById("to_print"),opt={margin:[20,20,20,20],filename:"file.pdf",image:{type:"jpeg",quality:.98},html2canvas:{scale:5},jsPDF:{unit:"pt",format:"a4",orientation:"portrait"}};html2pdf().from(element).set(opt).toPdf().get("pdf").then(function(e){var t=e.internal.getNumberOfPages();for(i=1;i<=t;i++)e.setPage(i),e.setFontSize(10),e.setTextColor(100),e.text("Devis Réf: D-A234-2301-001 - Page "+i+" of "+t,e.internal.pageSize.getWidth()/1.5,e.internal.pageSize.getHeight()-10)}).save();


/* <script src="https://cdnjs.cloudflare.com/ajax/libs/html2pdf.js/0.10.1/html2pdf.bundle.min.js"
    integrity="sha512-GsLlZN/3F2ErC5ifS5QtgpiJtWd43JWSuIgh7mbzZ8zBps+dvLusV+eNQATqgA/HdeKFVgA5v3S/cIrLF7QnIg=="
    crossorigin="anonymous" referrerpolicy="no-referrer"></script>
*/