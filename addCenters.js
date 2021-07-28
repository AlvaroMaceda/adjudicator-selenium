// THIS DOESN'T WORK!!

const codes = [
'46025799',
'46014224',
]

const addRowBtn = document.querySelector('[title="Añadir fila"]')
function addCode(code) {
  let lastInput
  let code = '46025799'
  addRowBtn.click()
  lastInput = Array.from(document.querySelectorAll('input[name="centre"]')).slice(-1)[0]
  lastInput.focus()
  lastInput.value = code
  addRowBtn.focus()
}

codes.forEach(addCode)




