package com.br.biblioteca.JPA_PostgreSQL;

import dao.*;
import model.*;
import util.JPAUtil;

import javax.persistence.EntityManager;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class App {
    public static void main(String[] args) throws IOException {

        //Criando instância da EntityManager para poder começar as transações no banco de dados
        EntityManager em = JPAUtil.getEntityManager();

        //Criando as instâncias das classes DAO
        LivroDAO livroDAO = new LivroDAO(em);
        EditoraDAO editoraDAO = new EditoraDAO(em);
        CategoriaDAO categoriaDAO = new CategoriaDAO(em);
    }
}