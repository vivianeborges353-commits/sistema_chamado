import streamlit as st

st.title("sistema de chamados")


if"chamados" not in st.session_state:
    st.session_state.chamados = []

st.subheader("abrir chamado")
titulo = st.text_input("titulo do chamado")
descricao= st.text_area("descrição de serviço")

if st.button("abrir chamado"):
    if titulo !="" and descricao != "":

        chamado = {
            "titulo": titulo,
            "descricao": descricao,
            "status": "aberto"
        }
        st.session_state.chamados.append(chamado)
        st.success("chamado aberto com sucesso")

st.subheader("lista de chamados")
if len(st.session_state.chamados) == 0:
    st.warning("nenhum chamado aberto")

else:
    for i,chamado in enumerate(st.session_state.chamados):
        st.write(f"{chamado['titulo']}")
        st.write(f"descricao:{chamado['descricao']}")
        st.write(f"status:{chamado['status']}")


        novo_status = st.selectbox(
            "alterar status",
            ["aberto", "em andamento","finalizado"],
            key=f"status{i}"
        )

        if st.button("atualizar status", key=f"btn{i}"):
            st.session_state.chamados[i]["status"] = novo_status
            st.success("status atulizado!")
            st.rerun()
        st.divider()



