
function genPDF(){
  var doc = new jsPDF();
  doc.fromHTML($('#testdiv').get(0),20,20,{
                 'width':500 });

  doc.save('Test.pdf');


}













// <script>
//       $(function () {
//         $("#id_Valid_From").datetimepicker({
//           format : 'DD/MM/YYYY HH:mm',
//
//         });
//       });
//     </script>
