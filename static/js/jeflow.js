$(document).ready(function () {

  setTimeout(function () {
    $('.preloader').css('height', 0);
    setTimeout(function () {
      $('.preloader').children().hide();
    }, 200);
  }, 500);

  if ($('.modal').length) {
    $('select').select2({
      language: 'tr',
      placeholder: '---------',
      width: '100%',
      dropdownParent: $('.modal .modal-content')
    });
  } else {
    $('select').select2({
      language: 'tr',
      placeholder: '---------',
      width: '100%'
    });
  }

  var interval = setInterval(function () {
    var momentNow = moment();
    momentNow.locale('tr');
    $('#date-part').html(momentNow.format('DD MMMM YYYY'));
    $('#time-part').html(momentNow.format('HH:mm:ss'));
  }, 100);

  $('.table').DataTable({
    ordering: false,
    responsive: true,
    dom: 'Bflrtip',
    buttons: true,
    language: {
      url: 'https://cdn.datatables.net/plug-ins/1.12.1/i18n/tr.json'
    }
  });

  $('.textarea').summernote();

  const popoverTriggerList = document.querySelectorAll('[data-bs-toggle="popover"]');
  const popoverList = [...popoverTriggerList].map(popoverTriggerEl => new bootstrap.Popover(popoverTriggerEl));

  // Here we can adjust defaults for all color pickers on page:
  jscolor.presets.default = {
    palette: [
      '#000000', '#7d7d7d', '#870014', '#ec1c23', '#ff7e26', '#fef100', '#22b14b', '#00a1e7', '#3f47cc', '#a349a4',
      '#ffffff', '#c3c3c3', '#b87957', '#feaec9', '#ffc80d', '#eee3af', '#b5e61d', '#99d9ea', '#7092be', '#c8bfe7',
    ],
    //paletteCols: 12,
    hideOnPaletteClick: true,
    //width: 271,
    //height: 151,
    //position: 'right',
    //previewPosition: 'right',
    //backgroundColor: 'rgba(51,51,51,1)', controlBorderColor: 'rgba(153,153,153,1)', buttonColor: 'rgba(240,240,240,1)',
  }
});