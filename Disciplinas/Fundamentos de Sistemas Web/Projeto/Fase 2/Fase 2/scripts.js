document.getElementById('formCadastro').addEventListener('submit', function(event) {
  event.preventDefault();

  // Validação do formulário
  var nome = document.getElementById('nome').value;
  if (!nome) {
      alert("Por favor, preencha o nome.");
      return;
  }

  // Outros campos de validação

  alert("Cadastro realizado com sucesso!");
});

// Função de agendamento
function agendar() {
  var data = document.getElementById('dataAgendamento').value;
  if (!data) {
      alert("Por favor, selecione uma data para o agendamento.");
      return;
  }
  alert("Agendamento realizado para " + data);
}