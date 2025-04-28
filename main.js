let validation = new JustValidate('#form')
let selector = document.querySelector("#phone")
let masks = new Inputmask("+7(999) 999-99-99")
masks.mask(selector)

validation.addField("#name", [
    {
        rule:'required',
        errorMessage:'Введите имя'
        
        
    },
    {
        rule: 'minLength',
        value: 2,
        errorMessage:'минимум 2 символа '
    }
])

validation.addField("#email", [
    {
        rule:'required',
        errorMessage:'Введите почту'
    },
    {
        rule: 'email',
        errorMessage:'Неправильное написание'
    }
])

validation.addField("#phone", [
    {
        validator:(value)=>{
            const phone =selector.inputmask.unmaskedvalue()
            return Boolean(Number(phone) && phone.length > 0)
        },
        errorMessage:'Введите номер телефона'
    },
    {
        validator:(value)=>{
            const phone =selector.inputmask.unmaskedvalue()
            return Boolean(Number(phone) && phone.length === 10)
        },
        errorMessage:'Введите номер телефона полностью'
    }
])