Projeto organizador de arquivos em python. 
O objetivo deste documento é documentar e explicar como este codico funciona,
de maneira facil de entender , com uma explicação direta com o que acontece 
em cada linha de códico. 

1- Bloco - 
Import 'os' = quando usamos 'os' estamos utilizando a biblioteca responsavél para 
usar o sistema operacional de arquivos e pastas. 

. caminho_atual = os.getcwd() = o 'os.getcwd' é para saber em qual pasta o programa está rodando 
. arquivos = os.listdir(caminho_atual) = o 'os.listdir' é usado para abrir todos os arquivos dentro da pasta onde estamos. 

2 - Bloco - 
. pastas = {...} = esta parte é criado um dicionário com chaves e listas. 
Que serve para deixar claro se o arquivo tem esta extenção ele deve ir para lugar x. 

3 - Bloco - 
. for pasta in pastas: = analisa todas as pastas dentro do dicionário 'pastas' 
Como 'imagens','videos','documentos' 
. if not os.path.exists(pastas): = isso serve para saber existe esta pasta? 
. os.mkdir(pastas) = este comando é para criar a pasta . 

4 - Bloco - 
. for aquivo in arquivos: = serve para analisar um por um dos arquivos e pastas. 
. if os.path.isfile(arquivo): = essa linha serve para perguntar , isto é um arquivo? se sim continua. 
. extensao = os.path.splitext(arquivos)[1].lower() = esta estapa é para separar o nome do arquivo da extensão. 
. como por exemplo "nome" , ".txt" , e a função do [1] é para citar que é para usar a extensão ".txt"
. O .lower() serve para deixar tudo com letra minúscula. 
. for pasta, extensao in pasta.items(): = é usado para observar cada pasta que voçe criou e as extensões que cada uma aceita.
. if extensao in extensoes: = aqui fica a pergunta , a extensão pertence a este arquivo? 
se sim , significa que este arquivo pertence a esta pasta. 
. destino = os.path.join(pasta,arquivos) = isso é para montar o caminho completo do destino, ou seja vai ficar assim
"Imagens"+"fotos.pdf". 
. os.rename(arquivo/destino) = isso aqui é para mover o arquivo na pasta certa! 
. Break = finalisa esse bloco. 'Pare' 

5 - Bloco - 
. Print(Arquivos organizados com sucesso!) = Uma mensagem informando que o trabalho está concluido com sucesso. 
